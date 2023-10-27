#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;

void main() {
    vec2 st = gl_FragCoord.xy/u_resolution;
    vec2 mouse_normalizado = u_mouse/u_resolution;
    gl_FragColor = vec4(mouse_normalizado.y,mouse_normalizado.y,mouse_normalizado.y,1.0);
}