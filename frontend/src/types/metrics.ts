export interface KPIs {
  total_calls: number;
  answered_calls: number;
  asr: number;
  acd: number;
}

export interface ChartDataPoint {
  time_point: string;
  total_calls: number;
}

export interface MetricsResponse {
  kpis: KPIs;
  chart_data: ChartDataPoint[];
}
