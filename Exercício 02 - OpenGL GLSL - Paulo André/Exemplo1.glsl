// X/Y Checkerboard Pattern
//Este shader cria um padrão de tabuleiro de xadrez simples.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;
    vec3 color = mod(floor(uv.x * 8.0) + floor(uv.y * 8.0), 2.0) < 1.0 ? vec3(1.0) : vec3(0.0);
    gl_FragColor = vec4(color, 1.0);
}