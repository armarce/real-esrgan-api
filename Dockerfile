FROM continuumio/anaconda3:latest
RUN conda create --name real-esrgan-api python=3.10.9
RUN conda activate real-esrgan-api
RUN pip install \"fastapi[all]\" \"uvicorn[standard]\" gunicorn
RUN cd /home
RUN git clone https://github.com/armarce/real-esrgan-api.git
RUN cd /home/real-esrgan-api
RUN git clone https://github.com/xinntao/Real-ESRGAN.git
RUN cd Real-ESRGAN
RUN pip install basicsr
RUN pip install facexlib
RUN pip install gfpgan
RUN pip install -r requirements.txt
RUN python setup.py develop
#apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN apt update && sudo apt upgrade -y
RUN cd /root
RUN curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash -
RUN apt-get install nodejs -y
RUN npm install -g pm2

RUN cd /home/real-esrgan-api/src
#RUN pm2 start "uvicorn app:app --port 3000 --host 0.0.0.0" --name app
CMD ["pm2-runtime", "start 'uvicorn app:app --port 3000 --host 0.0.0.0' --name app"]