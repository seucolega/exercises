def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()
    if hey_bob == '':
        return 'Fine. Be that way!'
    is_a_question = hey_bob.endswith('?')
    is_a_scream = hey_bob.isupper()
    if is_a_question and is_a_scream:
        return "Calm down, I know what I'm doing!"
    if is_a_question:
        return 'Sure.'
    if is_a_scream:
        return 'Whoa, chill out!'
    return 'Whatever.'
