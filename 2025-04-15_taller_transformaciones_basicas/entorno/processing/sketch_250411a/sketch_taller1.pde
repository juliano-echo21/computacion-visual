void setup() {
  size(600, 600, P3D);
  noStroke();
}

void draw() {
  background(30);
  lights();

  float time = millis() / 1000.0;

  // Movimiento ondulado
  float wave = sin(time) * 100;

  // Rotación
  float angle = radians(frameCount);

  // Escalado cíclico
  float scaleFactor = 1 + 0.5 * sin(time * 2);

  // Centro del canvas
  translate(width/2, height/2, 0);

  pushMatrix();

  // Movimiento ondulado en X y Z
  translate(wave, 0, wave);

  // Rotación en Y y X
  rotateY(angle);
  rotateX(angle / 2);

  // Escala cíclica
  scale(scaleFactor);

  // Dibujar cubo
  fill(100, 200, 255);
  box(100);

  popMatrix();
}
