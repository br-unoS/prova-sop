# prova-sop
Deploy de Aplicação Streamlit na AWS EC2
Este guia explica como criar uma instância EC2 na AWS, configurar o ambiente Python, instalar as dependências necessárias, enviar seu arquivo app.py junto com dados e rodar a aplicação Streamlit que utiliza matplotlib.

1. Criar Instância EC2
Acesse o Console da AWS EC2.

Clique em "Launch Instance".

Escolha a Amazon Linux 2 ou Ubuntu Server 22.04 LTS como AMI (recomendo Ubuntu).

Escolha o tipo da instância (ex: t2.micro para grátis).

Configure o grupo de segurança para liberar as portas:

SSH (porta 22) para seu IP

TCP porta 8501 para acesso ao Streamlit (pode ser 0.0.0.0/0 para teste).

Crie ou selecione um par de chaves para acessar a instância (.pem).

Lance a instância.

2. Conectar à Instância EC2
No seu computador local (Windows, Linux ou Mac):

bash
Copiar
Editar
ssh -i /caminho/para/sua-chave.pem ubuntu@IP-PUBLICO-DA-EC2
Exemplo Windows PowerShell, estando na pasta da chave:

powershell
Copiar
Editar
ssh -i .\sua-chave.pem ubuntu@18.208.155.89
3. Atualizar e Instalar Python 3.12 (Ubuntu)
Por padrão pode ter Python 3.x, mas para garantir a versão 3.12:

bash
Copiar
Editar
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-dev python3-pip
Verifique versão:

bash
Copiar
Editar
python3.12 --version
4. Criar e Ativar Ambiente Virtual Python
bash
Copiar
Editar
python3.12 -m venv venv
source venv/bin/activate
Seu prompt mudará para indicar que o venv está ativo.

5. Instalar Streamlit, pandas e matplotlib
bash
Copiar
Editar
pip install --upgrade pip
pip install streamlit pandas matplotlib
6. Enviar Arquivos app.py e MS_Finan.csv para EC2
No seu computador local, no terminal PowerShell ou Bash, na pasta dos arquivos e da chave:

bash
Copiar
Editar
scp -i ./sua-chave.pem ./app.py ubuntu@IP-DA-EC2:~
scp -i ./sua-chave.pem ./MS_Finan.csv ubuntu@IP-DA-EC2:~
7. Rodar o App Streamlit
Na EC2, com o ambiente virtual ativado (venv):

bash
Copiar
Editar
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
8. Acessar no Navegador
Abra no navegador:

cpp
Copiar
Editar
http://IP-PUBLICO-DA-EC2:8501
