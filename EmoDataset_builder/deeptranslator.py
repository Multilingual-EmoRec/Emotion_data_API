from deep_translator import GoogleTranslator
import warnings

def translate(sentence, source='en', target='de'):
    """
        A function used to translate sentences based on the GoogleTranslator.
        The work focused on the DeepL Translator. However, this API is not for free.

        Attributes
        ----------
        sentence : str
            Input a sentence, which needs to be translated from source to target language.
        source : str
            Input initial language, which is used for the sentenced (default='en').
        target : str
            Input target language, which you want your sentence to be translated in (default='de').
    """
    warnings.warn("Internetverbindung muss erhalten bleiben. No Error handling")

    return GoogleTranslator(source=source, target=target).translate(sentence)

if __name__ == "__main__":
    #example print
    print(translate_texts("This is sentence, which needs to be translated in to German."))
    