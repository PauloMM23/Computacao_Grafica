//Sinusoidal Pattern
//Gera um padrão usando funções senoidais.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;
    vec3 color = 0.5 + 0.5 * sin(uv.xyx * 10.0);
    gl_FragColor = vec4(color, 1.0);
}
