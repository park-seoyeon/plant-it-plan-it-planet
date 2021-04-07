#STEP 1 BUILD VUE PROJECT 

FROM node:12.18.1-alpine AS build 
WORKDIR /app 
COPY package.json ./ 
RUN npm install 
COPY . . 
RUN npm run build

#STEP 2 CREATE NGINX SERVER 

FROM nginx:1.19.0-alpine As prod-stage 
COPY --from=build /app/dist /usr/share/nginx/html 
COPY default.conf /temp/default.conf
RUN envsubst /app < /temp/default.conf > /etc/nginx/conf.d/default.conf

EXPOSE 80 
CMD ["nginx","-g","daemon off;"]