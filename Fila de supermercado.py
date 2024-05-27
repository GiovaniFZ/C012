import threading
import time
import random
from queue import Queue

# Classe que representa um cliente do supermercado
class Customer:
    def __init__(self, id, items):
        self.id = id
        self.items = items
        self.arrival_time = 0  # Tempo de chegada do cliente
        self.service_start_time = 0  # Tempo em que o atendimento do cliente começou
        self.service_end_time = 0  # Tempo em que o atendimento do cliente terminou

# Classe que representa o caixa do supermercado
class Cashier(threading.Thread):
    def __init__(self, id, scheduler):
        super().__init__()
        self.id = id
        self.lock = threading.Lock()
        self.queue = Queue()
        self.running = True
        self.scheduler = scheduler

    def add_customer(self, customer):
        self.queue.put(customer)

    def serve_customer(self, customer):
        with self.lock:
            print(f"Cliente {customer.id} está sendo atendido pelo caixa {self.id}.")
            time.sleep(customer.items)  # Simula o tempo de serviço baseado na quantidade de itens
            print(f"Cliente {customer.id} foi atendido pelo caixa {self.id}.")
            customer.service_end_time = time.time()
            self.scheduler.record_times(customer)

    def run(self):
        while self.running or not self.queue.empty():
            if not self.queue.empty():
                customer = self.queue.get()
                customer.service_start_time = time.time()
                self.serve_customer(customer)

    def stop(self):
        self.running = False

# Classe que representa o escalonador FCFS
class FCFS_Scheduler:
    def __init__(self, cashiers):
        self.cashiers = cashiers
        self.total_waiting_time = 0
        self.num_customers_served = 0
        self.queue = Queue()  # Fila principal

    def add_customer(self, customer):
        customer.arrival_time = time.time()
        self.queue.put(customer)
        print(f"Cliente {customer.id} adicionado na fila principal, carregando {customer.items} itens.")

    def run(self):
        for cashier in self.cashiers:
            cashier.start()
        while not self.queue.empty():
            customer = self.queue.get()
            while True:
                for cashier in self.cashiers:
                    if cashier.queue.empty():
                        cashier.add_customer(customer)
                        self.num_customers_served += 1
                        break
                else:
                    time.sleep(0.1)
                    continue
                break
        for cashier in self.cashiers:
            cashier.stop()
            cashier.join()

    def record_times(self, customer):
        self.total_waiting_time += (customer.service_start_time - customer.arrival_time)

    def average_waiting_time(self):
        return self.total_waiting_time / self.num_customers_served if self.num_customers_served != 0 else 0

# Classe que representa o escalonador SJF
class SJF_Scheduler:
    def __init__(self, cashiers):
        self.cashiers = cashiers
        self.total_waiting_time = 0
        self.num_customers_served = 0
        self.queue = []

    def add_customer(self, customer):
        customer.arrival_time = time.time()
        self.queue.append(customer)
        print(f"Cliente {customer.id} adicionado na fila principal, carregando {customer.items} itens.")
        self.queue.sort(key=lambda x: x.items)  # Ordena a lista com base na quantidade de itens

    def run(self):
        for cashier in self.cashiers:
            cashier.start()
        while self.queue:
            for cashier in self.cashiers:
                if self.queue:
                    customer = self.queue.pop(0)
                    cashier.add_customer(customer)
                    self.num_customers_served += 1
        for cashier in self.cashiers:
            cashier.stop()
            cashier.join()

    def record_times(self, customer):
        self.total_waiting_time += (customer.service_start_time - customer.arrival_time)

    def average_waiting_time(self):
        return self.total_waiting_time / self.num_customers_served if self.num_customers_served != 0 else 0

# Função principal
def main():
    # Cria clientes com diferentes números de itens
    customers = [Customer(i, random.randint(1, 13)) for i in range(1, 10)]

    # Cria dois caixas para a simulação FCFS
    cashiers = [Cashier(i, None) for i in range(1, 3)]

    # Executa o escalonador FCFS
    print("FCFS Scheduler:")
    fcfs_scheduler = FCFS_Scheduler(cashiers)
    for cashier in cashiers:
        cashier.scheduler = fcfs_scheduler
    for customer in customers:
        fcfs_scheduler.add_customer(customer)
    fcfs_scheduler.run()
    fcfs_avg_waiting_time = fcfs_scheduler.average_waiting_time()
    print(f"Tempo médio de espera: {fcfs_avg_waiting_time:.2f} segundos")

    # Cria novas instâncias de caixas para a simulação SJF
    cashiers = [Cashier(i, None) for i in range(1, 3)]

    # Executa o escalonador SJF
    print("\nSJF Scheduler:")
    sjf_scheduler = SJF_Scheduler(cashiers)
    for cashier in cashiers:
        cashier.scheduler = sjf_scheduler
    for customer in customers:
        sjf_scheduler.add_customer(customer)
    sjf_scheduler.run()
    sjf_avg_waiting_time = sjf_scheduler.average_waiting_time()
    print(f"Tempo médio de espera: {sjf_avg_waiting_time:.2f} segundos")

    # Comparação dos tempos de espera médio
    print("\nComparação:")
    print(f"Tempo médio de espera do FCFS: {fcfs_avg_waiting_time:.2f} segundos")
    print(f"Tempo médio de espera do SJF: {sjf_avg_waiting_time:.2f} segundos")

    if fcfs_avg_waiting_time < sjf_avg_waiting_time:
        print("FCFS tem um menor tempo médio de espera.")
    elif sjf_avg_waiting_time < fcfs_avg_waiting_time:
        print("SJF tem um menor tempo médio de espera.")
    else:
        print("Ambos tem o mesmo tempo médio de espera.")

if __name__ == "__main__":
    main()
