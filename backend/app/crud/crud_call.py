from sqlalchemy.orm import Session
from sqlalchemy import func, case

from app.models.call import Call
from app.schemas.call import CallCreate

class CrudCall:

    def get_by_call_id(self, db: Session, *, call_id: str) -> Call | None:
        """
        Busca uma chamada pelo seu ID externo para evitar duplicatas.
        """
        return db.query(Call).filter(Call.call_id == call_id).first()

    def create(self, db: Session, *, obj_in: CallCreate) -> Call:
        """
        Cria um novo registro de chamada no banco de dados.
        """
        db_obj = Call(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Call]:
        """
        Recupera uma lista de chamadas com paginação.
        """
        return db.query(Call).order_by(Call.call_date.desc()).offset(skip).limit(limit).all()
    
    def get_kpi_data(self, db: Session) -> dict:
        """
        Executa uma única query para buscar todos os dados brutos para os KPIs.
        """
        # Define as expressões para evitar repetição
        answered_case = case((Call.sip_code == 200, 1), else_=0)
        duration_case = case((Call.sip_code == 200, Call.duration), else_=0)

        # O .first() é usado porque a query de agregação retorna uma única linha
        result = db.query(
            func.count(Call.id).label("total_calls"),
            func.sum(answered_case).label("answered_calls"),
            func.sum(duration_case).label("total_duration_answered")
        ).first()

        return result._asdict() if result else {}
    
    def get_chart_data(self, db: Session) -> list:
        """
        Busca dados de chamadas agrupados por hora para o gráfico.
        """
        result = db.query(
            func.date_trunc('hour', Call.call_date).label('time_point'),
            func.count(Call.id).label('total_calls')
        ).group_by(
            func.date_trunc('hour', Call.call_date)
        ).order_by(
            func.date_trunc('hour', Call.call_date)
        ).all()

        return result

# Instância única para ser usada em toda a aplicação
call = CrudCall()
