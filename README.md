# 🌿🎵 Scent-Music Molecular Cryptography (SMMK)

Doğanın kimyasal yapısını ve müziğin akustik boyutunu birleştiren, çok katmanlı özgün bir şifreleme algoritması

---

## 🏛️ Akademik Geçerlilik

Bu çalışma, **5th International Conference on Recent Academic Studies (ICRAS 2025)** bünyesinde sunulmuştur.

Proje; geleneksel siber güvenlik yaklaşımlarına kimya, müzik ve bilgisayar bilimlerini entegre ederek disiplinlerarası bir yaklaşım sunmaktadır. Bu yönüyle literatürde özgün bir konuma sahiptir.

Bu GitHub deposu, bildiride sunulan teorik modelin yazılım implementasyonunu içermektedir.

---

## 🌟 Proje Hakkında

**Scent-Music Molecular Cryptography (SMMK)**, dijital veriyi doğanın kimyasal yapı taşlarıyla şifreleyen, Sultan Karapınar tarafından tasarlanmış özgün bir algoritmadır.

Bu sistemde bir mesaj yalnızca karakterlerden oluşmaz:

- Her harf → bir moleküle  
- Her molekül → kimyasal formüle  
- Her formül → kendine özgü bir **Akustik Parmak İzi**ne  

dönüşür.

Amaç; bilginin sadece görsel olarak değil, aynı zamanda işitsel olarak da temsil edildiği sinestezik (duyular arası) bir güvenlik katmanı oluşturmaktır.

---

## 🧠 Algoritmik Mimari

Algoritma, metin tabanlı veriyi dört ana katmanda işler:

---

### 1️⃣ Moleküler Haritalama

Alfabedeki her karakter, doğadaki karakteristik koku profillerine göre tarafımdan eşleştirilmiştir.

Örnek:

A → Vanilin  
B → Mentol  
C → Limonen  

---

### 2️⃣ Formülasyon ve Ayrıştırma

Sistem, eşleşen kokunun gerçek kimyasal formülünü analiz eder.

Örnek:

Girdi: "A"  
İşlem: Vanilin → C8H8O3  

Regex tabanlı ayrıştırma yöntemi ile elementler ve atom sayıları belirlenir.

---

### 3️⃣ Akustik Kodlama (Elementel Notalar)

Her temel atom, fiziksel ve sembolik karakterine uygun bir nota ve tını ile temsil edilir:

| Element  | Sembol | Nota | Enstrüman Karakteri |
|----------|--------|------|---------------------|
| Karbon   | C      | Do   | Piyano (Tok ve Kararlı) |
| Hidrojen | H      | Re   | Keman (Keskin ve Akıcı) |
| Oksijen  | O      | Mi   | Flüt (Yumuşak ve Saf) |
| Azot     | N      | Fa   | Bas (Derin ve Dolgun) |

---

### 4️⃣ İşitsel Çıktı ve Dekriptaj

Elementlerin formüldeki sayısal dağılımına göre bir melodi dizisi oluşturulur.

Ortaya çıkan çıktı:

- Şifreli bir veri temsilidir.
- Aynı zamanda molekülün duyusal (akustik) bir yansımasıdır.

Dekriptaj süreci, bu akustik yapıdan tersine moleküler eşleşme mantığı ile gerçekleştirilir.

---

## 🎨 Arayüz Özellikleri

- Dinamik arka plan (Gaussian Blur destekli görsel panel)
- Gerçek zamanlı ses motoru (Pygame tabanlı sentezleyici)
- Thread yapısı sayesinde donmayan kullanıcı deneyimi
- Modern Tkinter tabanlı grafik arayüz
- Nota dinletme özelliği

---

## 🔊 Ses Motoru

Sistem, notaları hazır ses dosyaları kullanmadan üretir.

NumPy ile matematiksel sinüs dalgaları oluşturulur ve Pygame aracılığıyla gerçek zamanlı olarak çalınır.

Bu yapı sayesinde her molekül, kendine özgü bir akustik imza üretir.

---

## 🛠️ Teknik Gereksinimler

Projeyi çalıştırmak için aşağıdaki kütüphaneler gereklidir:

```bash
pip install pygame numpy pillow


## 🚀 Nasıl Kullanılır?

GitHub üzerinden depoyu klonlayın.

python sifreleme_algoritmasi.py komutuyla uygulamayı başlatın.

Mesajınızı girip ŞİFRELE deyin ve DİNLET butonuyla mesajınızın melodisini keşfedin!


