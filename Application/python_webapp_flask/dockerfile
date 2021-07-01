# for syntax details, see https://docs.docker.com/engine/reference/builder/
FROM python:3
RUN pip install flask
# TODO install requests module
RUN python -m pip install requests
# TODO expose port 5000
EXPOSE 5000
# TODO copy todolist.py, index.html
COPY . /app
# I needed to specify the directory
WORKDIR /app
# TODO launch the application
CMD python todolist.py
