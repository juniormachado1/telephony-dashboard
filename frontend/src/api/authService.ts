import apiClient from './client';
import { AxiosError } from 'axios';

interface LoginCredentials {
  username?: string;
  password?: string;
}

interface LoginResponse {
  access_token: string;
  token_type: string;
}

interface ErrorResponse {
  detail: string;
}

export const loginUser = async (
  credentials: LoginCredentials
): Promise<LoginResponse> => {
  const formData = new URLSearchParams();
  formData.append('username', credentials.username || '');
  formData.append('password', credentials.password || '');

  try {
    const response = await apiClient.post<LoginResponse>(
      '/auth/login',
      formData,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    );
    return response.data;
  } catch (error) {
    const axiosError = error as AxiosError;

    const errorData = axiosError.response?.data;

    if (
      errorData &&
      typeof errorData === 'object' &&
      'detail' in errorData
    ) {
      throw new Error((errorData as ErrorResponse).detail);
    }

    throw new Error('Erro ao fazer login');
  }
};
