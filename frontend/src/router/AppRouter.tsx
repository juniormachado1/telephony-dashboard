import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from '../pages/LoginPage';
import DashboardPage from '../pages/DashboardPage';
import ProtectedRoute from '../components/ProtectedRoute';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* Rota pública de login */}
        <Route path="/login" element={<LoginPage />} />

        {/* Rota raiz redireciona para o dashboard. 
            O ProtectedRoute vai decidir se mostra ou redireciona para /login */}
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        {/* Agrupamento de Rotas Protegidas */}
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          {/* Outras rotas protegidas podem ser adicionadas aqui no futuro */}
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default AppRouter;