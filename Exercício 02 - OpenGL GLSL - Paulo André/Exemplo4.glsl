//Ruído de Simplex
//Um exemplo usando ruído Simplex para criar uma textura.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar ruído Simplex em 2D
float simplex(vec2 p) {
    return 0.5 + 0.5 * sin(p.x * 10.0 + p.y * 10.0);
}

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;
    float n = simplex(uv * 5.0); // Ajuste a escala conforme necessário
    gl_FragColor = vec4(vec3(n),1.0);
}
