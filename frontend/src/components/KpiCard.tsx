import { Card, CardContent, Typography } from '@mui/material';

interface KpiCardProps {
  title: string;
  value: string | number;
  color?: string;
}

const KpiCard: React.FC<KpiCardProps> = ({ title, value, color = 'text.primary' }) => (
  <Card>
    <CardContent>
      <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
        {title}
      </Typography>
      <Typography variant="h5" component="div" sx={{ color }}>
        {value}
      </Typography>
    </CardContent>
  </Card>
);

export default KpiCard;