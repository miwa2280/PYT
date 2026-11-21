FROM python:3.14.8-slim

WORKDIR /project

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && mv /root/.local/bin/uv /usr/local/bin/uv \
    && mv /root/.local/bin/uvx /usr/local/bin/uvx

COPY pyproject.toml uv.lock /project/
RUN uv pip install --system --no-cache .

COPY /project /project

CMD ["uv", "run", "-m", "main", "11"]