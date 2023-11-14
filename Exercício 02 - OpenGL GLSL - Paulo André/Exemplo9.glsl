//Ruído de Worley (Voronoi) Animado
//Um shader que gera um padrão de células Voronoi animado.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar ruído de Worley (Voronoi)
float worley(vec2 p, float time) {
    vec2 cell = floor(p);
    vec2 f = fract(p);

    float dist = 1.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 offset = vec2(float(x), float(y));
            vec2 point = cell + offset + 0.5 * sin(time) * vec2(sin(time), cos(time));
            float d = length(point - p);
            dist = min(dist, d);
        }
    }

    return dist;
}

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;

    // Ajuste a escala e a velocidade para controlar a aparência do ruído
    float scale = 10.0;
    float timeFactor = 3.5;

    // Gere o valor de ruído de Worley animado
    float time = u_time;

    float worleyNoise = worley(gl_FragCoord.xy * scale, time * timeFactor);
    gl_FragColor = vec4(vec3(worleyNoise), 1.0);
}
