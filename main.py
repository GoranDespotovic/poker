import random
import time

lst = [str(x) for x in range(10, 101)]

kasa = 1000
cip1 = 0
while cip1 not in lst:
  cip1 = input(f'каса:{kasa}\nунесите жељени износ чипа од 10 до 100. ')
cip = int(cip1)

if cip > kasa:
  cip = kasa
print('\n')
while kasa > 0:
  kasa -= cip
  print(f'каса: {kasa} динара чип: {cip} динара')
  high = ['A', 'J', 'Q', 'K']
  odelo = ['пик ', 'срце', 'каро', 'треф']
  brojevi = ['2', '3', '4', '5', '6', '7', '8', '9', '1']
  red = ['2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A', 'џ']
  pet_istih = False
  u_nizu = False
  u_boji = False
  poker = False
  ful = False
  kenta = False
  tri_iste = False
  dva_para = False
  par = False

  spil = [
    'џокер ', 'џокер ', 'џокер ', 'џокер ', '2 пик ', '2 срце', '2 каро',
    '2 треф', '3 пик ', '3 срце', '3 каро', '3 треф', '4 пик ', '4 срце',
    '4 каро', '4 треф', '5 пик ', '5 срце', '5 каро', '5 треф', '6 пик ',
    '6 срце', '6 каро', '6 треф', '6 пик ', '7 срце', '7 каро', '7 треф',
    '8 пик ', '8 срце', '8 каро', '8 треф', '9 пик ', '9 срце', '9 каро',
    '9 треф', '10пик ', '10срце', '10каро', '10треф', 'A пик ', 'A срце',
    'A каро', 'A треф', 'J пик ', 'J срце', 'J каро', 'J треф', 'Q пик ',
    'Q срце', 'Q каро', 'Q треф', 'K пик ', 'K срце', 'K каро', 'K треф'
  ]
  k = ['_', '_', '_', '_', '_']

  def krt():
    print(k[0], '|', k[1], '|', k[2], '|', k[3], '|', k[4])

  dobitak = 0
  ulog = cip

  x = random.choice(spil)
  k[0] = x
  spil.remove(x)
  x = random.choice(spil)
  k[1] = x
  spil.remove(x)
  x = random.choice(spil)
  k[2] = x
  spil.remove(x)
  x = random.choice(spil)
  k[3] = x
  spil.remove(x)
  x = random.choice(spil)
  k[4] = x
  spil.remove(x)
  #k = ['6 треф','9 треф','10 пик','џокер ','џокер ']
  krt()

  p = input(
    f'за повећавање/смањивање чипа  унесите број 9\n\nзадржи {k[0]}? 0 за ДА ')
  if p == '9':
    cip2 = 0
    while cip2 not in lst:
      cip2 = input(
        f'каса: {kasa} тренутни чип: {cip}\nунесите жељени износ чипа од 10 до 100. '
      )
    cip = int(cip2)
    krt()

    p = input(f'задржи {k[0]}? 0 за ДА ')
  if p != '0':
    x = random.choice(spil)
    k[0] = x
    spil.remove(x)
  p = input(f'задржи {k[1]}? 0 за ДА ')
  if p != '0':
    x = random.choice(spil)
    k[1] = x
    spil.remove(x)
  p = input(f'задржи {k[2]}? 0 за ДА ')
  if p != '0':
    x = random.choice(spil)
    k[2] = x
    spil.remove(x)
  p = input(f'задржи {k[3]}? 0 за ДА ')

  if p != '0':
    x = random.choice(spil)
    k[3] = x
    spil.remove(x)
  p = input(f'задржи {k[4]}? 0 за ДА ')
  if p != '0':
    x = random.choice(spil)
    k[4] = x
    spil.remove(x)

  krt()
  broj = 1
  slike = []
  naznaka = []
  vrednosti = []
  boje = []
  zbir_boja = []
  redni_brojevi = []

  for i in k:
    naznaka.append(i[:1])
    naznaka.sort()
  for i in k:
    boje.append(i[2:])
  for i in odelo:
    zbir_boja.append(boje.count(i))
  for i in brojevi:
    vrednosti.append(naznaka.count(i))
  for i in high:
    slike.append(naznaka.count(i))
  for i in naznaka:
    redni_brojevi.append(red.index(i))
    redni_brojevi.sort()

  #print('naznaka',naznaka)
  #print('slike',slike)
  #print('vrednosti',vrednosti)
  #print('zbir_boja',zbir_boja)
  #print('redni brojevi',redni_brojevi)
  if naznaka.count('џ') == 1 and redni_brojevi[0] == redni_brojevi[
      1] and redni_brojevi[1] == redni_brojevi[2] and redni_brojevi[
        2] == redni_brojevi[3] or naznaka.count('џ') == 2 and redni_brojevi[
          0] == redni_brojevi[1] and redni_brojevi[2] == redni_brojevi[
            1] or naznaka.count('џ') == 3 and redni_brojevi[
              0] == redni_brojevi[1] or naznaka.count('џ') == 4:
    pet_istih = True

  if redni_brojevi[4] == redni_brojevi[3] + 1 and redni_brojevi[
      3] == redni_brojevi[2] + 1 and redni_brojevi[2] == redni_brojevi[
        1] + 1 and redni_brojevi[1] == redni_brojevi[0] + 1 or naznaka.count(
          'џ'
        ) == 3 and redni_brojevi[1] - redni_brojevi[0] > 0 and redni_brojevi[
          1] - redni_brojevi[0] < 5 or naznaka.count(
            'џ'
          ) == 2 and redni_brojevi[2] - redni_brojevi[0] > 0 and redni_brojevi[
            2] - redni_brojevi[0] < 5 and redni_brojevi[1] < redni_brojevi[
              2] and redni_brojevi[1] > redni_brojevi[0] or naznaka.count(
                'џ') == 1 and redni_brojevi[3] - redni_brojevi[
                  0] > 1 and redni_brojevi[3] - redni_brojevi[
                    0] < 5 and redni_brojevi[1] < redni_brojevi[
                      3] and redni_brojevi[1] > redni_brojevi[
                        0] and redni_brojevi[2] < redni_brojevi[
                          3] and redni_brojevi[2] > redni_brojevi[
                            0] and redni_brojevi[1] < redni_brojevi[2]:
    u_nizu = True
  #print(u_nizu)

  if zbir_boja.count(5) == 1 or zbir_boja.count(4) and naznaka.count(
      'џ') == 1 or zbir_boja.count(3) and naznaka.count(
        'џ') == 2 or zbir_boja.count(2) and naznaka.count('џ') == 3:
    u_boji = True
  #print(u_boji)
  for i in slike:
    for x in vrednosti:
      if i == 4 or x == 4 or i == 3 and 'џ' in naznaka or x == 3 and 'џ' in naznaka or naznaka.count(
          'џ') == 3 or i == 2 and naznaka.count(
            'џ') == 2 or x == 2 and naznaka.count('џ') == 2:
        poker = True
  if 2 in slike and 3 in slike or 2 in vrednosti and 3 in vrednosti or 2 in slike and 3 in vrednosti or 2 in vrednosti and 3 in slike or naznaka.count(
      'џ') == 1 and 2 in slike and 2 in vrednosti or naznaka.count(
        'џ') == 1 and vrednosti.count(2) == 2 or naznaka.count(
          'џ') == 1 and slike.count(2) == 2:
    ful = True
  if 3 in vrednosti or 3 in slike or 2 in vrednosti and 'џ' in naznaka or naznaka.count(
      'џ') == 2 or 2 in slike and 'џ' in naznaka:
    tri_iste = True
  if vrednosti.count(2) == 2 or slike.count(2) == 2 or (
      vrednosti.count(2) == 1 and slike.count(2) == 1):
    dva_para = True
  if 2 in slike or 1 in slike and naznaka.count('џ') == 1:
    par = True
  if pet_istih:
    dobitak += ulog * 1100
    print(f'ПЕТ ИСТИХ {dobitak} динара')
  elif u_boji and u_nizu and redni_brojevi[0] > 7:
    dobitak += ulog * 500
    print(f'РОЈАЛ ФЛЕШ {dobitak} динара')

  elif u_boji and u_nizu:
    dobitak += ulog * 100
    print(f'СТРЕЈТ ФЛЕШ {dobitak} динара')

  elif poker:
    dobitak += ulog * 40
    print(f'ПОКЕР {dobitak} динара')

  elif ful:
    dobitak += ulog * 10
    print(f'ФУЛ {dobitak} динара')
  elif u_boji and not u_nizu:
    dobitak += ulog * 7
    print(f'БОЈА {dobitak} динара')
  elif not u_boji and u_nizu:
    dobitak += ulog * 5
    print(f'КЕНТА {dobitak} динара')
  elif tri_iste:
    dobitak += ulog * 3
    print(f'ТРИ ИСТЕ {dobitak} динара')

  elif dva_para:
    dobitak += ulog * 2
    print(f'ДВА ПАРА {dobitak} динара')

  elif par:
    dobitak += ulog
    print(f'ПАР СЛИКА {dobitak} динара')
  if dobitak > 0:

    x = 0
    while x < 11:
      kocka = ''

      while kocka != '1' and kocka != '2' and kocka != '3' and kocka != '4':
        print(f'тренутни улог {dobitak} динара')
        kocka = input('мања(1) / већа(2) / пола(3) / каса(4) ')

        pogoodjaj = ''

        if kocka == '1':
          pogodjaj = 'мања'
        elif kocka == '2':
          pogodjaj = 'већа'
        elif kocka == '3':
          pogodjaj = '3'
        elif kocka == '4':
          pogodjaj = '4'
        #elif kocka == '5':
        #pogadjaj = '5'
        sanse = ('мања', 'већа')
        manja_veca = random.choice(sanse)

        if pogodjaj == '4':
          dobitak = dobitak
          x = 11
          break
        elif pogodjaj == manja_veca:
          dobitak *= 2
          print(f'{manja_veca} ПОГОДИЛИ СТЕ!')

          x += 1
          time.sleep(0.5)
        elif pogodjaj == '3':
          if dobitak < 20:
            dobitak == dobitak
          elif dobitak >= 20:
            dobitak = dobitak // 2
            kasa += dobitak

        elif pogodjaj != manja_veca:
          print(f'{manja_veca} НИСТЕ ПОГОДИЛИ:(')
          time.sleep(0.5)
          dobitak = 0
          x = 11
          break
          time.sleep(0.5)

  if kasa < 1:
    print(f'ОСТАЛИ СТЕ БЕЗ ПРЕБИЈЕНЕ ПАРЕ!\nПОТРАЖИТЕ ПОМОЋ...')
    break

  kasa += dobitak
  if kasa >= 100000:
    print(f'ЧЕСТИТАМО!\nосвојили сте {kasa} динара\nДовиђења:)')
    break

  print('')
  time.sleep(1)
