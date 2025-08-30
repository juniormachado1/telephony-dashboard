import { create } from 'zustand';
import { getMetrics, getCalls } from '../api/dashboardService';
import type { KPIs, ChartDataPoint } from '../types/metrics';
import type { Call } from '../types/calls';

interface DashboardState {
  kpis: KPIs | null;
  chartData: ChartDataPoint[];
  calls: Call[];
  isLoading: boolean;
  error: string | null;
  fetchDashboardData: () => Promise<void>;
}

export const useDashboardStore = create<DashboardState>((set) => ({
  kpis: null,
  chartData: [],
  calls: [],
  isLoading: false,
  error: null,
  fetchDashboardData: async () => {
    set({ isLoading: true, error: null });
    try {
      const [metricsData, callsData] = await Promise.all([
        getMetrics(),
        getCalls(),
      ]);
      set({
        kpis: metricsData.kpis,
        chartData: metricsData.chart_data,
        calls: callsData,
        isLoading: false,
      });
    } catch (err: unknown) {
      const errorMessage =
        err instanceof Error ? err.message : 'An unknown error occurred';
      set({ error: errorMessage, isLoading: false });
    }
  },
}));