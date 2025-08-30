import apiClient from './client';
import type { MetricsResponse } from '../types/metrics';
import type { Call } from '../types/calls';

export const getMetrics = async (): Promise<MetricsResponse> => {
  const response = await apiClient.get('/metrics/');
  return response.data;
};

export const getCalls = async (): Promise<Call[]> => {
  const response = await apiClient.get('/calls/');
  return response.data;
};