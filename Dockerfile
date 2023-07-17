FROM continuumio/anaconda3:latest
RUN conda create --name real-esrgan-api python=3.10.9
SHELL ["conda", "run", "-n", "real-esrgan-api", "/bin/bash", "-c"]
RUN pip install "fastapi[all]" "uvicorn[standard]" gunicorn
WORKDIR /home
RUN git clone https://github.com/armarce/real-esrgan-api.git
WORKDIR /home/real-esrgan-api
RUN git clone https://github.com/xinntao/Real-ESRGAN.git
WORKDIR /home/real-esrgan-api/Real-ESRGAN
RUN pip install basicsr
RUN pip install facexlib
RUN pip install gfpgan
RUN pip install -r requirements.txt
RUN python setup.py develop
# apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN apt-get update && apt-get upgrade -y
WORKDIR /root
RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash
RUN apt-get install nodejs -y
RUN npm install -g pm2

WORKDIR /home/real-esrgan-api/src
#RUN pm2 start "uvicorn app:app --port 3000 --host 0.0.0.0" --name app
CMD ["pm2-runtime", "app.py"]