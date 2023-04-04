# Use chatGPT to classify the input text into one of the given categories
import openai
import json
import sys

# OpenAI API key
# add your key here
openai.api_key = "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"

# function to classify text into one of the given categories
def classify(text, categories):
    response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", #Modelo do LLM. Você pode usar a versão anterior para comparar
            messages =[
                {"role": "system", "content": f"Você é um assistente encarregado de ler o resumo de uma apresentação da área de História \
                    e escolher uma categoria para classificá-la. A lista de possibilidades de tags é a seguinte: {categories}. \
                    Você se esforçará para escolher tags que tenham maior relação com o contido no texto. Evite tags não-relacionadas"},
                {"role": "user", "content": f"Analise este resumo da apresentação: {text} e selecione a tag mais adequada. \
                    Dê o resultado em formato json com as chaves 'categoria' e 'motivo da escolha'"}],
            max_tokens=100, #Máximo de "créditos" que ele vai usar para tentar a resposta
            top_p=0.1,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
    return response['choices'][0]['message']['content']

# list of categories
categories = ['trabalho','memória','trajetórias','associativismo','raça',\
    'performances culturais','família','educação','ensino de história','história pública',\
    'história digital','história oral','pós-abolição','história da escravidão','gênero']

# list of texts
text1 = ['Este Simpósio Temático quer trazer para o debate o protagonismo de mulheres – e aqui estamos entendendo como mulheres as pessoas que assim se identificam, portanto, mulheres trans estão previstas no debate. Serão bem-vindas pesquisas que discutam as mulheres que se candidataram a cargos, sendo eleitas ou não, as que ocuparam cargos tendo sido nomeadas, além da análise de suas ausências. Espera-se também pesquisas que focalizem narrativas de trajetórias de mulheres, sejam elas artistas, religiosas, empresárias, operárias, participantes de movimentos sociais, movimentos de bairro, enfim, mulheres “mandonas”.']
text2 = ['Vinte anos após a promulgação da Lei n. 10.639/03 e quinze da Lei n. 11.645/08, temos um acúmulo de pesquisas, práticas e publicações sobre o ensino de história e culturas africanas, afro-brasileiras, indígenas e da educação das relações étnico-raciais no Brasil. A descolonização curricular é um dos desafios colocados por tais marcos legais e implica o rompimento com uma matriz epistêmica eurocêntrica e baseada numa concepção de sujeito universal. Nesse sentido, este ST busca congregar professoras/es e pesquisadoras/es dos diversos espaços educativos, interessadas/os na desconstrução dos discursos hegemônicos e que desenvolvem saberes emancipatórios no âmbito do antirracismo. Ancorados nas “pedagogias de combate ao racismo”, temos interesse nas seguintes abordagens: descolonização curricular e práticas transgressoras em diferentes espaços educativos; narrativas, metodologias e epistemologias contra-hegemônicas sobre as populações negras e indígenas; patrimônio cultural, história pública e ensino-aprendizagem de história; materiais didáticos, cidadania digital e tecnologias para o ensino de história; avaliação do alcance das Leis em diferentes comunidades (quilombolas, camponesas, de terreiro etc.), instituições educativas e espaços de produção e circulação do conhecimento.']
text3 = ['Este Simpósio Temático, vinculado ao GT Emancipações e Pós-Abolição, objetiva reunir pesquisadores(as) e professores(as) dispostos a refletir, aprofundar e compartilhar suas experiências de pesquisa e ensino sobre a temática. Em atenção aos processos de emancipação e às lutas por liberdade e cidadania anteriores à assinatura da Lei de 13 de maio de 1888, consideramos importante destacar o papel que pessoas escravizadas, libertas e livres “de cor” desempenharam, por meio de suas trajetórias individuais e/ou coletivas, assim como aprofundar as discussões sobre os significados da liberdade, abolicionismos e lutas por direitos e conquista de lugares sociais diversos. Tendo em vista o pós-abolição como conceito e temporalidade, conforme pontuam Frederick Cooper, Thomas Holt e Rebeca Scott, e como problema histórico, conforme Ana Lugão Rios e Hebe Mattos, interessa-nos refletir acerca das construções identitárias em jogo no referido período, bem como suas implicações políticas, conteúdos culturais e transformações ao longo dos séculos XIX e XX. Almeja-se congregar pesquisas com foco nas configurações sociais estabelecidas no pós-Abolição e nos processos de construção e ampliação da liberdade, com recortes cronológicos anteriores e posteriores à Lei de 13 de maio.']

# Call function

classify(text1, categories)
