# Use the official Python image as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir selenium

# Make port 4444 available to the world outside this container
EXPOSE 4444

# Run the YouLikeHits script when the container launches
CMD ["python", "./auto.py"]
