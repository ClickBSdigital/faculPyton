from database import execute_query


class ReportSystem:
    @staticmethod
    def gerar_relatorio_vagas():
        query = """
        SELECT 
            (SELECT COUNT(*) FROM veiculos WHERE hora_saida IS NULL) as ocupadas,
            (SELECT max_vagas FROM config WHERE id = 1) as total_vagas
        """
        dados = execute_query(query)[0]
        return {
            "ocupadas": dados["ocupadas"],
            "disponiveis": dados["total_vagas"] - dados["ocupadas"],
            "total": dados["total_vagas"],
        }

    @staticmethod
    def gerar_relatorio_fluxo(data_inicio, data_fim):
        query = """
        SELECT 
            DATE(hora_entrada) as data,
            COUNT(*) as entradas,
            SUM(CASE WHEN hora_saida IS NOT NULL THEN 1 ELSE 0 END) as saidas
        FROM veiculos
        WHERE hora_entrada BETWEEN %s AND %s
        GROUP BY DATE(hora_entrada)
        ORDER BY data
        """
        return execute_query(query, (data_inicio, data_fim))
