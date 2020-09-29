from typing import Optional

from thinc.api import Model

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .lemmatizer import UkrainianLemmatizer
from ...language import Language
from ...lookups import Lookups


class UkrainianDefaults(Language.Defaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS


class Ukrainian(Language):
    lang = "uk"
    Defaults = UkrainianDefaults


@Ukrainian.factory(
    "lemmatizer",
    assigns=["token.lemma"],
    default_config={"model": None, "mode": "pymorphy2", "lookups": None},
    default_score_weights={"lemma_acc": 1.0},
)
def make_lemmatizer(
    nlp: Language,
    model: Optional[Model],
    name: str,
    mode: str,
    lookups: Optional[Lookups],
):
    return UkrainianLemmatizer(nlp.vocab, model, name, mode=mode, lookups=lookups)


__all__ = ["Ukrainian"]
