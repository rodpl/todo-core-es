FROM microsoft/dotnet:1.0.0-core

COPY . /app

WORKDIR /app

EXPOSE 5000/tcp

ENTRYPOINT ["dotnet", "ToDo.Web.dll", "--server.urls=http://0.0.0.0:5000"]
