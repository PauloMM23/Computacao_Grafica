//Ruído Perlin 2D
//Este shader cria um padrão de ruído Perlin em duas dimensões.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar ruído Perlin em 2D
float noise(vec2 p) {
    return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;
    float n = noise(uv * 5.0); // Ajuste a escala do ruído conforme necessário
    gl_FragColor = vec4(vec3(n), 1.0);
}
