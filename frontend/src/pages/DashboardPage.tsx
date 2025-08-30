import React, { useEffect } from 'react';
import { useAuthStore } from '../store/authStore';
import { useNavigate } from 'react-router-dom';
import { useDashboardStore } from '../store/dashboardStore';
import { AppBar, Box, Button, Container, Toolbar, Typography, Grid, CircularProgress, Alert, Card, CardContent } from '@mui/material';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { DataGrid } from '@mui/x-data-grid';
import type { GridColDef } from '@mui/x-data-grid';
import KpiCard from '../components/KpiCard';

const DashboardPage: React.FC = () => {
  const navigate = useNavigate();
  const { logout } = useAuthStore();
  const { kpis, chartData, calls, isLoading, error, fetchDashboardData } = useDashboardStore();

  useEffect(() => {
    fetchDashboardData();
  }, [fetchDashboardData]);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'call_date', headerName: 'Data/Hora', width: 180 },
    { field: 'source', headerName: 'Origem', width: 130 },
    { field: 'destination', headerName: 'Destino', width: 130 },
    { field: 'duration', headerName: 'Duração (s)', type: 'number', width: 120 },
    { field: 'sip_code', headerName: 'SIP Code', type: 'number', width: 110 },
    { field: 'cost', headerName: 'Custo', type: 'number', width: 110 },
  ];

  if (isLoading) {
    return <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}><CircularProgress /></Box>;
  }

  if (error) {
    return <Alert severity="error">Erro ao carregar dados do dashboard: {error}</Alert>;
  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Dashboard de Telefonia
          </Typography>
          <Button color="inherit" onClick={handleLogout}>Logout</Button>
        </Toolbar>
      </AppBar>
      <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={6} md={3}><KpiCard title="Total de Chamadas" value={kpis?.total_calls ?? 0} /></Grid>
          <Grid item xs={12} sm={6} md={3}><KpiCard title="Atendidas" value={kpis?.answered_calls ?? 0} color="green" /></Grid>
          <Grid item xs={12} sm={6} md={3}><KpiCard title="ASR (Taxa de Atendimento)" value={`${kpis?.asr ?? 0}%`} /></Grid>
          <Grid item xs={12} sm={6} md={3}><KpiCard title="ACD (Duração Média)" value={`${kpis?.acd ?? 0}s`} /></Grid>

          <Grid item xs={12}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>Total de Chamadas por Hora</Typography>
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart data={chartData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="time_point" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="total_calls" stroke="#8884d8" name="Total de Chamadas" />
                  </LineChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </Grid>

          <Grid item xs={12}>
            <Card>
              <Box sx={{ height: 400, width: '100%' }}>
                <DataGrid
                  rows={calls}
                  columns={columns}
                  initialState={{
                    pagination: {
                      paginationModel: { pageSize: 5 },
                    },
                  }}
                  pageSizeOptions={[5, 10, 20]}
                  checkboxSelection
                />
              </Box>
            </Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default DashboardPage;