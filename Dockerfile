# Use the official python image as a base image
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

#Copy the requirements file intyo the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code into the directory
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the main application
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

