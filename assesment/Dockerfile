#NodeJS as the base image
FROM node:18

#Setting the working directory in the container
WORKDIR /usr/src/app

#Copy package.json and package-lock.json
COPY package*.json ./

#Installing dependencies
RUN npm install

#Copy others files in the container directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["node", "server.js"]