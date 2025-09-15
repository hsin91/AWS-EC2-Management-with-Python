import boto3
import time

def criar_instancia(ec2_client, ami_id, instance_type, key_name):
    """Cria e inicia uma nova instância EC2."""
    print("Criando instância...")
    try:
        response = ec2_client.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            KeyName=key_name
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instância {instance_id} criada. Aguardando estado de 'running'...")
        
        # Espera a instância estar em estado "running"
        waiter = ec2_client.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        
        return instance_id
    except Exception as e:
        print(f"Erro ao criar a instância: {e}")
        return None

def listar_instancias(ec2_client):
    """Lista todas as instâncias EC2 e seus estados."""
    print("Listando instâncias EC2...")
    try:
        response = ec2_client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                print(f"ID da Instância: {instance_id}, Estado: {state}")
    except Exception as e:
        print(f"Erro ao listar instâncias: {e}")

def parar_instancia(ec2_client, instance_id):
    """Para uma instância EC2 específica."""
    print(f"Parando instância {instance_id}...")
    try:
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Instância {instance_id} em processo de parada.")
    except Exception as e:
        print(f"Erro ao parar a instância: {e}")

def terminar_instancia(ec2_client, instance_id):
    """Termina (exclui) uma instância EC2 específica."""
    print(f"Terminando instância {instance_id}...")
    try:
        ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(f"Instância {instance_id} em processo de término.")
    except Exception as e:
        print(f"Erro ao terminar a instância: {e}")

if __name__ == "__main__":
    # Certifique-se de que suas credenciais da AWS estão configuradas
    # via `aws configure` ou variáveis de ambiente.
    ec2 = boto3.client('ec2', region_name='us-east-1') # Altere a região se necessário

    # Parâmetros para a nova instância
    AMI_ID = 'ami-053b0d53c279acc91'  # Exemplo: Amazon Linux 2 AMI
    INSTANCE_TYPE = 't2.micro'
    KEY_NAME = 'nome-da-sua-chave'   # Substitua pelo nome da sua chave EC2

    # Exemplo de uso
    # Descomente a função que você quer executar

    # 1. Criar e iniciar uma instância
    # instance_id_criada = criar_instancia(ec2, AMI_ID, INSTANCE_TYPE, KEY_NAME)
    # print(f"\nInstância criada com ID: {instance_id_criada}")

    # 2. Listar todas as instâncias
    # listar_instancias(ec2)

    # 3. Parar uma instância (substitua o ID)
    # parar_instancia(ec2, 'i-0123456789abcdef0')

    # 4. Terminar uma instância (substitua o ID)
    # terminar_instancia(ec2, 'i-0123456789abcdef0')
