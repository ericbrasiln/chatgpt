def tag(title):
    tags = ['História Antiga','História Medieval','História Moderna','História Contemporânea']
    response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", #Modelo do LLM. Você pode usar a versão anterior para comparar
            messages =[
                {"role": "system", "content": f"Você é um assistente encarregado de ler o título de uma reportagem e escolher uma categoria para classificá-la. A lista de possibilidades de tags é a seguinte: {tags}. Você se esforcará para escolhar tags que tenham maior relação com o contido no texto. Evite tags não-relacionadas"},
                {"role": "user", "content": f"Analise este título de matéria jornalística: {title} e selecione a tag mais adequada. Dê o resultado em formato json com as chaves 'categoria' e 'motivo da escolha'"}],
            max_tokens=100, #Máximo de "créditos" que ele vai usar para tentar a resposta
            top_p=0.1,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
    return response['choices'][0]['message']['content']

