//Padrão de Espiral
//Um shader que gera um padrão de espiral.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;
    float angle = atan(uv.y - 0.5, uv.x - 0.5);
    float radius = length(uv - vec2(0.5));
    float pattern = mod(floor(angle * radius * 10.0), 2.0) < 1.0 ? 1.0 : 0.0;
    gl_FragColor = vec4(vec3(pattern), 1.0);
}
