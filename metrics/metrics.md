4 tipos de métricas:
Gauge: Valores que vão variar, subir e descer. Por exemplo: 
    - Temperatura.
    - Quantidade de pessoas.
    - Posição (Lat/Long).
    - Consumo de memória.
    - CPU.

Counter: Soma incremental. Exemplos:
    - Contagem de requests com status code 200.
    - Contagem de requests com status 5xx.
    - request_total. "total" no nome, normalmente.

Histogram: 0 - 10 segundos. Bucket de 0.5s~1.0s, Bucket de 1.0s~1.5s ... Exemplos:
    - time_response_bucket: Vai gravar as métricas dentro do bucket do range em questão pra facilitar a consulta depois de forma agrupada.
    - É como se fosse uma partição? Pra facilitar as consultas?
    - requests_duration_seconds_bucket{le="0.5"} -> Query pra buscar as requests que duraram até 0.5s.
    - Pode-se customizar o número e valores de buckets.
    - le = less or equal.

Summary: 0 - 1. O tipo de dado summary é bem parecido com o histogram, com a diferença que os buckets, aqui chamados de quantiles, são definidos por um valor entre 0 e 1, ou seja, o valor do bucket é o valor que está entre os quantiles.

    -Da mesma forma como no histogram, podemos criar métricas do tipo summary com alguns itens importantes adicionados ao final do nome da métrica, por exemplo:

    -requests_duration_seconds_sum{instance="localhost:8899",job="Primeiro Exporter"}
    Utilizamos o sufixo _sum indica que o valor é uma soma, ou seja, o valor é somado a cada vez que a métrica é atualizada e o sufixo _count para indicar que o valor é um contador, ou seja, o valor é incrementado a cada vez que a métrica é atualizada.

    -O ponto alto do summary é a excelente precisão e o ponto baixo é a baixa flexibilidades, pois percentuais e as janelas de tempos precisam ser definidos durante a criação da métrica e não é possível agregar métricas do tipo summary com outras métricas do tipo summary durante a criação das queries.

    O quantil do Summary é o percentil:
        - 0.9, quero pegar as métricas do percentil 90, 90% das requisições elas tiveram o valor = ou menor que 100ms.
        - 0.99, quero pegar as me´tricas do percentil 99, 99 das requisições que tiveram o valor ou menor que 150ms.
        - 0.5%, quero pegar as métricas/requests do percentil 50, 50% das requisições estão até esse peso/valor/tempo.

