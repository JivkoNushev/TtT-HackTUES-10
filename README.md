# TtTranquil
<div align="center">
  <img src="https://github.com/JivkoNushev/TtT-HackTUES-10/assets/54147006/bfe486a6-8504-4b99-9776-bdf6c2c95fa3" alt="drawing" style="width:500px;"/>
</div>
<p>
    Нашият проект цели да намали шума, генериран от товарните кораби в океана, с цел подобряване на хабитата на морските обитатели.
  Презентация: https://docs.google.com/presentation/d/1d2f0oHlDBZD9BUe0prROIdK4We9mLg90cDdkX2PxlHM/edit?usp=sharing
</p>
  
## Тема: 
<div align="center">
  <img src="https://github.com/JivkoNushev/TtT-HackTUES-10/assets/54147006/62c3eaf8-657d-4cae-8908-2faf422574e2" alt="drawing" style="width:400px;"/>
  <p>🌊 Exploring the Infinite Ocean 🌊</p>
</div>

## Проблемът

<div>
  <img align="left" src="https://github.com/JivkoNushev/TtT-HackTUES-10/assets/54147006/5bc11aa0-baa6-4149-9547-f767928adf62" alt="drawing" style="width:400px;"/>

  <p> Проучвания показват, че подводният шум, излъчван от двигателите и най-вече от перките на търговските кораби, може да има както краткосрочни, така и дългосрочни отрицателни последици за морските обитатели. </p>
  <p> Въпреки че този шум може да изглежда безобиден на пръв поглед, постоянното му присъствие представлява значителен риск за морските обитатели, като нарушава тяхната комуникация, навигация и поведение при хранене. </p>
  <p> Има множество регулаторни усилия на организации като Международната морска организация (ММО) и Международната организация на труда (МОТ) за цялостно решаване на проблема. Въпреки тези усилия, корабният шум продължава да бъде проблем и до днес. </p>
  
  <br clear="left"/>
</div>


## Решението
<div>
  <img align="left" src="https://github.com/JivkoNushev/TtT-HackTUES-10/assets/50800277/a3e73175-6854-4096-9b5f-905b9f041fe8" alt="drawing" style="width:400px;"/>

  <p> Решението на нашия проблем е заглушаването на двигателите на големите кораби. За релизацията на този проект се изпозлва водоустойчиви микрофон и говорител, два esp32 и raspberry-pi. </p>
  <p> Микрофонът е закачен за шамандура и потопен под вода. Шамандурата е свързана за кораба и по въжето е пуснат водоустойчив кабел, който свърва микрофона и модул за честота. Този модул подава информацията на esp32 и то я праща на raspberry-pi, използвайки MQTT протокол за комуникация. </p>
  <p> Raspberry-pi обработва данните, които се изпращат на другото esp32 по MQTT. При засичане на звуковите вълни на перката се засичат и външни звукови вълни на животни или дори други кораби. Прави се Фурие анализ на засечените вълни, за да се разграничат външните шумове и да се изолират само тези, генерирани от перката. След разпознаването на шума, се прилага деструктивна интерференция - вълните, със същата честота и амплитуда, се дефазират на 180 градуса, за да може при издаването им да се занижат вълните, генерирани от перката. Тези изградени вълни се изпращат на другото esp32 по MQTT. </p>
  <p> Второто esp32 е свързано с усилвател и говорител, поставен около перката на кораба, който възпроизвежда шума, който му е бил изпратен. </p>
  
  <br clear="left"/>
</div>

## Бъдещо развитие
<div>
  <p> Бъдещото развитие на проекта включва покупката на нужния хардуер, поради липсата на финансиране. За разпознаването на шума от мотора и по-точно изключване на външни шумове може да се използва изкуствен интелект. </p>
</div>

## Технологии
<div>
  <li>esp32</li>
  <li>raspberry-pi</li>
  <li>Python</li>
  <li>Embedded</li>
</div>

#### Протоколи
<div>
  <li>MQTT</li>
</div>


## Отбор
 - Александър Кюмурков (ментор)
 - Виктор (капитан)
 - Митко
 - Живко
 - Ива
 - Йоан
