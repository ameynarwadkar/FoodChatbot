# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY backend/package*.json ./

# Install dependencies
RUN npm install

COPY backend .

WORKDIR /frontend

COPY frontend/build ./build

WORKDIR /app
# Expose the port on which your backend server runs
EXPOSE 3000

# Command to run your backend server
CMD ["node", "index.js"]
