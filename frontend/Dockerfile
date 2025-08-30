FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Gera os arquivos estáticos otimizados para produção
RUN npm run build

# Nginx para servir os arquivos estáticos
FROM nginx:1.25-alpine

# Copia os arquivos de build do estágio anterior
COPY --from=builder /app/dist /usr/share/nginx/html

# Remove a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia nossa configuração customizada do Nginx
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]