from apps.kols.factories import KolsFactory


def run():
    KolsFactory.create_batch(100)