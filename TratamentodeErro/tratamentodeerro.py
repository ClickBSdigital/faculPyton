try:
    a = int(input("Digite uma palavra: "))
except ValueError:
    print("Digite apenas número!!")
except:
    print("Erro Desconhecido !!!!")
finally:
    print(f"Final do Algoritino, valor de a: {a}")    
print("="*60)
print("""
       __|__
--@--@--(_)--@--@--
    """)
    
print()