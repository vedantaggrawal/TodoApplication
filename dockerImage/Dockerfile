FROM python:3

LABEL maintainer="vedant.aggrawal@gmail.com"

RUN groupadd -r todo && useradd -r -s /bin/false -g todo todo

ENV PYTHONUNBUFFERED 1


RUN mkdir -p /etc/todo/conf

COPY . /etc/todo/
WORKDIR /etc/todo
RUN pip install -r requirements.txt && \
	 rm -rf requirements.txt && \
         chown -R todo:todo /etc/todo

EXPOSE 8000
USER todo
ENTRYPOINT ["python","manage.py", "runserver"]
CMD ["0.0.0.0:8000"]
