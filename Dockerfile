FROM python:3.9-alpine3.14

WORKDIR /usr/src/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .

RUN apk update \
  && apk upgrade \
  && apk add \
    --virtual .dependencies build-base binutils \
  && pip install --no-cache-dir -v -r requirements.txt \
  && apk del .dependencies

CMD ["/bin/sh"]
#CMD [ "python", "./your-daemon-or-script.py" ]