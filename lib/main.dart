import 'package:flutter/material.dart';

void main() {
  runApp(const QuoteApp());
}

class QuoteApp extends StatelessWidget {
  const QuoteApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Quote App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const QuoteHomePage(),
    );
  }
}

class QuoteHomePage extends StatefulWidget {
  const QuoteHomePage({super.key});

  @override
  State<QuoteHomePage> createState() => _QuoteHomePageState();
}

class _QuoteHomePageState extends State<QuoteHomePage> {
  final List<String> quotes = [
    'Believe you can and you are halfway there.',
    'Success is the sum of small efforts repeated every day.',
    'Do something today that your future self will thank you for.',
    'Dream big, work hard, stay focused, and surround yourself with good people.',
    'The only way to do great work is to love what you do.',
  ];

  final List<String> quoteImages = [
    'assets/images/quote_mountain.png',
    'assets/images/quote_habits.png',
    'assets/images/quote_future.png',
    'assets/images/quote_teamwork.png',
    'assets/images/quote_creative_work.png',
  ];

  int currentIndex = 0;

  void showNextQuote() {
    setState(() {
      currentIndex = (currentIndex + 1) % quotes.length;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF5F7FB),
      appBar: AppBar(
        title: const Text('Motivational Quote App'),
        centerTitle: true,
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
      ),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 520),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.emoji_events, size: 70, color: Colors.amber),
                  const SizedBox(height: 24),
                  Card(
                    elevation: 4,
                    clipBehavior: Clip.antiAlias,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        AspectRatio(
                          aspectRatio: 16 / 9,
                          child: Image.asset(
                            quoteImages[currentIndex],
                            width: double.infinity,
                            fit: BoxFit.cover,
                          ),
                        ),
                        Padding(
                          padding: const EdgeInsets.all(24),
                          child: Text(
                            quotes[currentIndex],
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              fontSize: 22,
                              fontWeight: FontWeight.w500,
                              height: 1.4,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 30),
                  ElevatedButton(
                    onPressed: showNextQuote,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.indigo,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(
                        horizontal: 32,
                        vertical: 14,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                    child: const Text(
                      'Next Quote',
                      style: TextStyle(fontSize: 18),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
