tickers = {
    'AFLT' : ['Аэрофлот'],
    'VTBR' : ['ВТБ'],
    'GAZP' : ['ГАЗПРОМ'],
    'GMKN' : ['ГМКНорНик', 'ГМКНорНикель', 'Норникель'],
    'LKOH' : ['ЛУКОЙЛ'],
    'MTSS' : ['МТС'],
    'MGNT' : ['Магнит'],
    'MOEX' : ['МосБиржа'],
    'NLMK' : ['НЛМК'],
    'ROSN' : ['Роснефть'],
    'RTKM' : ['Ростелеком'],
    'HYDR' : ['РусГидро'],
    'SBER' : ['Сбербанк', 'Сбер'],
    'CHMF' : ['Северсталь'],
    'SNGS' : ['Сургутнефтегаз'],
    'PLZL' : ['Полюс', 'ПолюсЗолото'],
    'YNDX' : ['Yandex'],
    'NVTK' : ['Новатэк'],
    'TATN' : ['Татнефть'],
    'SNGSP' : ['Сургутнефтегаз-п'],
    'TRNFP' : ['Транснефть-п'],
    'ASTR' : ['Астра'],
    'ALRS' : ['АЛРОСА'],
    'SBERP' : ['Сбербанк-п'],
    'MTLR' : ['Мечел'],
    'TCSG' : ['TCS', 'Тинькофф'],
    'MAGN' : ['ММК'],
    'FLOT' : ['Совкомфлот'],
    'PHOR' : ['ФосАгро'],
    'POLY' : ['Polymetal', 'Полиметал'],
    'RUAL' : ['РУСАЛ'],
    'SMLT' : ['Самолет'],
    'VKCO' : ['Вконтакте', 'VK'],
    'OZON' : ['OZON', 'ОЗОН'],
    'SOFL' : ['iСофтлайн', 'Софтлайн'],
    'SIBN' : ['Газпромнефть'],
    'FIVE' : ['FIVE', 'Пятерочка'],
    'AFKS' : ['Система', 'АФКСистема'],
    'IRAO' : ['ИнтерРАО'],
    'BSPB' : ['БСП'],
    'NMTP' : ['НМТП'],
    'BELU' : ['НоваБев'],
    'FESH' : ['ДВМП'],
    'POSI' : ['iПозитив', 'ПозитивТехнолоджис', 'PositiveTechnologies'],
    'TRMK' : ['ТМК'],
    'RNFT' : ['Русснефть'],
    'SGZH' : ['Сегежа'],
    'BANEP' : ['Башнефть-п'],
    'RASP' : ['Распадская'],
    'CBOM' : ['МКБ'],
    'FEES' : ['Россети'],
    'SELG' : ['Селигдар'],
    'TATNP' : ['Татнефть-п'],
    'ROLO' : ['Русолово'],
    'PIKK' : ['ПИК'],
    'UPRO' : ['Юнипро'],
    'AGRO' : ['AGRO'],
    'MSNG' : ['МосЭнерго'],
    'GLTR' : ['GLTR'],
    'SVAV' : ['СОЛЛЕРС'],
    'KMAZ' : ['КАМАЗ'],
    'TGKA' : ['ТГК-1'],
    'MTLRP' : ['Мечел'],
    'UNAC' : ['iАвиастК'],
    'IRKT' : ['Яковлев-3'],
    'OGKB' : ['ОГК-2'],
    'GTRK' : ['ГТМ'],
    'ENPG' : ['ЭН+ГРУП'],
    'AQUA' : ['ИНАРКТИКА'],
    'AMEZ' : ['АшинскийМЗ'],
    'BLNG' : ['Белон'],
    'GECO' : ['iГЕНЕТИКО'],
    'LSRG' : ['ЛСР'],
    'ABIO' : ['iАРТГЕН'],
    'LIFE' : ['iФармсинтз'],
    'AKRN' : ['Акрон'],
    'MVID' : ['Мвидео'],
    'WUSH' : ['iВУШХолднг'],
    'NKHP' : ['НКХП'],
    'FIXP' : ['FIXP'],
    'CARM' : ['СТГ'],
    'TTLK' : ['Таттелеком'],
    'BANE' : ['Башнефть'],
    'LSNG' : ['РСетиЛЭ'],
    'VSMO' : ['ВСМПО-АВСМ'],
    'QIWI' : ['iQIWI', 'Киви'],
    'ELFV' : ['ЭЛ5Энер'],
    'RTKMP' : ['Ростел-п'],
    'LNZLP' : ['Лензолото-п'],
    'ABRD' : ['АбрауДюрсо'],
    'MSTT' : ['Мостотрест'],
    'MRKP' : ['РСетиЦП'],
    'KZOSP' : ['КазаньОргСинтез-п'],
    'APTK' : ['Аптеки36и6'],
    'GCHE' : ['ГруппаЧеркизово'],
    'KZOS' : ['КазаньОргСинтез'],
    'DVEC' : ['ДЭК'],
    'LSNGP' : ['РСетиЛЭ-п'],
    'LNZL' : ['Лензолото'],
    'MRKC' : ['РоссЦентр'],
    'RENI' : ['Ренессанс'],
    'KROT' : ['КрассныйОктябрь'],
    'TGKN' : ['ТГК-14'],
    'NKNC' : ['НКНХ'],
}

def get_tickers():
    companies = {}
    for ticker in tickers:
        for name in tickers[ticker]:
            companies[name.lower()] = ticker
    return tickers, companies

