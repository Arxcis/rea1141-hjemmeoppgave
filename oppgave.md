# Hjemmeoppgave

*Matematikk 1 for ingeniørfag (REA1141)* - frist 17.11.17 (kl 23:59)

```yaml
navn: Jonas Johan Solsvik
kull: 16HBPROGA
linje: Programmering [APP|SPILL]
institutt: Datateknologi og Informatikk 
fakultet: Informasjonsteknologi og Elektroteknikk
sted: NTNU Gjøvik    
```

### Oppgave

Tanken med obligen er å anvende matematikk i en praktisk oppgave gjennom bruk av derivasjon, integrasjon og/eller diff.likninger.

Du må selv definere et problem og løse dette.  Ikke fortvil, vi stiller ikke skyhøye krav.

**NB! **  Sy sammen besvarelsen din til ett dokument (helst PDF eller Wordfil) før du laster det opp i Blackboard. 

### Egen oppgavetekst

Jeg har kjøpt meg elbil, og skal på min første 'roadtrip'. Jeg har bestemt meg for å kjøre fra *Lindesnes* til *Nordkapp*. Hva er optimal hastighet? Om jeg kjører fort, kommer jeg fortere frem, men må bruke lengre tid på å lade.

**Datainnsamlingi**

1. **Distanse**
   Raskeste veg går igjennom sverige, 2364km[^1], i følge google maps.  Jeg ønsker heller å kjøre en litt 		lengre veg igjennom Norge, 2533km.[^2] 

$$
D = 2533km
$$



2. **Kapasitet**
   Elbilen jeg har kjøpt er en Tesla Model S AWD P100D med 100kwh batteri. [^3]

$$
Batterikapasitet = 100kWh  \\
$$



<br><br><br><br><br><br><br>

3. **Forbruk per hastighet** 

   ![rangevsconsumption](speedvsconsumption.jpg)

   *Image: Tesla.com blog - Model S efficiency and range fra 2012*[^4]

   Grafen ovenfor er hentet fra Tesla sin offisielle blog i 2012

   ![](speedvsconsumption.png)

   ​	**Formel fra Wolframalpha**
   $$
   forbruk(hastighet) = f(v) = 0.0714v^{2} - 3.523v + 239.203 \ (Wh/mile), \\ v=[5,70] 
   $$
   ​


4. **Tid per prosent lading**

   Hvor lang tid tar det å lade fra 60-80 prosent sammenlik med med fra 40-60 prosent. Data for dette har jeg hentet fra en youtube-video[^6] av en Tesla-eier som har tatt tiden på hvor fort bilen sin lader fra 0-90% fulladet (0kWh - 90kWh). 

   ![](socvst.png)
   ​	**Formel fra Wolframalpha**

$$
Ladetid(StateOfCharge) = 0.00289soc^{2} + 0.4034soc + 2.197 \ (t_{min}), \\ soc=[0,91]
$$

<br>

<br>

#### OPPGAVE A)

Jeg starter med fulladet bil. Første etappe til min første ladestopp er 200Km. Hvor mye energi i kWh bruker bilen på den første etappen?

Vi har allerede "forbrukshastighet" fra dataene. Da er det bare å lage et bestemt integral for å få totalforbruket. Vi integrerer med hensyn på kilometer:
$$
BestemtForbruk(km, v) = \int_{start_{km}}^{slutt_{km}} forbruk(v) \ dkm
\\
BestemtForbruk(v)  = \int_{0}^{200} (0.0714v^{2} - 3.523v + 239.203)  \ dkm 
\\
= \bigg(  (0.0714v^{2} - 3.523v + 239.203) \ km \bigg)_0^{200}
\\  
= \underline{ (0.0714v^{2} - 3.523v + 239.203) \times 200 \times (0.6214 mile/km)}
$$
Vi antar at forbruket er konstant for en gitt hastighet men, i en bil med fossilt drivstoff, så vil forbruket også være en funksjon av kilometer, fordi etterhvert som en bruker opp drivstoffet, så blir bilen lettere og forbruket går dermed ned. I en elektrisk bil trenger vi ikke å ta hensynet til dette, siden drivstoffet er elektroner som har negliserbar vekt. Forbruket varierer også som en funksjon av vindretning, vindhastighet, høydemeter både opp og ned.

**Utskrift**

```
Kjører 200km i ulike hastigheter:
--------------------------------
    km/h   kwh/km  Forbruk kWh
---------------------------------
	 40 	0.122 	 24.33
	 50 	0.123 	 24.69
	 60 	0.129 	 25.74
	 70 	0.137 	 27.47
	 80 	0.149 	 29.90
	 90 	0.165 	 33.00
	100 	0.184 	 36.79
	110 	0.206 	 41.27
	120 	0.232 	 46.43
	130 	0.261 	 52.28
	140 	0.294 	 58.81
	150 	0.330 	 66.03
	160 	0.370 	 73.94
	170 	0.413 	 82.53
```

<br><br><br><br><br>
<br>
<br>
<br>

#### OPPGAVE B)

Jeg starter med 100% (100kWh) kapasitet på batteriet. Hva er "State of Charge"(SOC) i % når jeg kommer frem til første lader etter 200km?
$$
LadestartSOC(v) = startkWh - BestemtForbruk(v)
\\
= \underline{100kWh - (0.0714v^{2} - 3.523v + 239.203) \times 200 \times (0.6214 mile/km))}
$$
```
Kjører 200km i ulike hastigheter:
----------------------------
  km/h  State of charge[%]  
----------------------------
	 40 	 75.67
	 50 	 75.31
	 60 	 74.26
	 70 	 72.53
	 80 	 70.10
	 90 	 67.00
	100 	 63.21
	110 	 58.73
	120 	 53.57
	130 	 47.72
	140 	 41.19
	150 	 33.97
	160 	 26.06
	170 	 17.47
```



<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br><br>

####OPPGAVE C)

Hvor lang tid tar det for meg å lade opp til  90% som en funksjon av hastighet *v*, før jeg kan kjøre videre? Gitt at jeg started med 100% kapasitet?
$$
BestemtLadetid(v) = \int_{Start_{SOC}(v)}^{Slutt_{SOC}} Ladetid \ '(soc) \ dsoc
\\
= \bigg(Ladetid(soc) \bigg)_{Start_{SOC}(v)}^{Slutt_{SOC}}
\\
=Ladetid(Slutt_{SOC}) - Ladetid(Start_{SOC}(v))
\\
=Ladetid(Slutt_{SOC}) - Ladetid(startkWh - TotalForbruk(v)))
\\
=Ladetid(Slutt_{SOC}) - Ladetid((startkWh - \int_{start_{km}}^{slutt_{km}} forbruk(v) \ dkm)
\\
=Ladetid(Slutt_{SOC}) - Ladetid(startkWh - (forbruk(v)\times slutt_{km} - forbruk(v) \times start_{km})
$$
<br>


Gitt at:

- SluttSOC = 90%

- startkWh = 100kWh(100%)

- sluttkm = 200km

- startkm = 0km

$$
BestemtLadetid(v) = ( 0.00289\times 90^{2} + 0.4034\times 90 + 2.197 ) \\ -  Ladetid(100 - (0.0714v^{2} - 3.523v + 239.203) \times 200 \times (0.6214))
$$

```
Kjører 200km i ulike hastigheter:
---------------------------------
    km/h   Lade til 90%[min]  
---------------------------------
	 40 	        13
	 50 	        13
	 60 	        14
	 70 	        15
	 80 	        17
	 90 	        20
	100 	        23
	110 	        26
	120 	        30
	130 	        34
	140 	        38
	150 	        43
	160 	        47
	170 	        52
```



<br>

<br>

<br>

#### OPPGAVE D)

Hva er totaltiden brukt, kjøretid + ladetid som en funksjon av v ?
$$
Kjoretid(v) = \frac{km}{v}
\\
Totaltid(v) = BestemtLadetid(v) + Kjoretid(v)
$$

```
Kjører 200km i ulike hastigheter:
--------------------------------------------------------
    km/h   Kjøretid[min]  + Lade 90%[min] =  Total tid    
--------------------------------------------------------
	 40 	    300 	         13 	          313
	 50 	    240 	         13 	          253
	 60 	    200 	         14 	          214
	 70 	    171 	         15 	          187
	 80 	    150 	         17 	          167
	 90 	    133 	         20 	          153
	100 	    120 	         23 	          143
	110 	    109 	         26 	          135
	120 	    100 	         30 	          130
	130 	     92 	         34 	          126
	140 	     86 	         38 	          124
	150 	     80 	         43 	          123
	160 	     75 	         47 	          122
	170 	     71 	         52 	          122
```

<br>

<br>

<br>

#### OPPGAVE F)

Hvilken hastighet er den idelle hastigheten, for å minimere den totale kjøre+ladetiden ?
For å finne det så må vi finne nullpunktet av den deriverte *Totaltid ' (v)*
$$
Totaltid \ ' (v)  = \bigg( BestemtLadetid(v) + Kjoretid(v) \bigg)' = 0
\\
Totaltid \ ' (v)  =  BestemtLadetid \ '(v) + Kjoretid \ '(v) = 0
$$
Dette blir en veldig stygg derivasjon som jeg ikke har tenkt til å gjøre. En kan likevel se ut i fra tabellen ovenfor at dette nullpunktet må ligge i nærheten av *170 km/h.

<br><br>

<br>

<br>

<br>

<br>

### Konklusjon

- Ladehastigheten på elektriske biler har blitt så rask, at det alltid lønner seg tidsmessig å kjøre raskest mulig fra A - B, innenfor lovlige grenser, selv om dette vil føre til betydelig lengre ladetid. 
- Du vil likevel nå et punkt der hastigheten, og forbruket deretter, blir så stor at du ikke vil nå destinasjonen din. Dette vil sette et tak på hvor fort det er teoretisk mulig å komme frem.
- Dersom du er begrenset på økonomi i stedet for tid, så vil det motsatte gjelde. Du vil bruke mindre og mindre penger dess saktere du har mulighet til å kjøre. Elekstriske biler er veldig effektive selv i lave hastigheter.

[^1]: Sweedish-route ,  https://goo.gl/maps/JYmrfFJHUJ42 - 15.11.17
[^2]: Norwegian-route, https://goo.gl/maps/ukhx6uGBVx82 - 15.11.17
[^3]: Tesla energy consumption, https://en.wikipedia.org/wiki/Tesla_Model_S#Energy_consumption - 15.11.17
[^4]: Tesla blog model s efficiency, https://www.tesla.com/no_NO/blog/model-s-efficiency-and-range?redirect=no - 15.11.17
[^5]: WolframAlpha.com, https://www.wolframalpha.com/ - 15.11.17
[^6]: Supercharging P100D to 90%, Bjorn Nyland, https://youtu.be/qS3ulrEhLAg, - 15.11.17






