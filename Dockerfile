FROM python:3.8
WORKDIR /app_my
COPY . .
ENV FLASK_APP /app_my/findSponsor.py
RUN pip install -r requirements.txt
EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]