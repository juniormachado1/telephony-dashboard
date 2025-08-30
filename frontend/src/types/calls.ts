export interface Call {
  id: number;
  call_id: string;
  call_date: string;
  source: string;
  destination: string;
  duration: number;
  sip_code: number;
  cost: number;
}