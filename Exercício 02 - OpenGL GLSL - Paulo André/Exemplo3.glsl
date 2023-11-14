//Mandelbrot Fractal
//Renderiza o conjunto de Mandelbrot.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;
    vec2 c = uv * 3.0 - 2.0;
    vec2 z = c;
    float intensity = 0.0;
    for (int i = 0; i < 100; i++) {
        z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + c;
        if (length(z) > 2.0) {
            intensity = float(i) / 100.0;
            break;
        }
    }
    gl_FragColor = vec4(vec3(intensity), 1.0);
}
