#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main(){
    vec2 st = gl_FragCoord.xy/u_resolution;
    float pct = 0.0;
 //A distância do píxel em relação ao centro - ponto (0.5, 0.5)
    pct = distance(st,vec2(0.5));
 //Se a distância for maior que 0.5, pct recebe 1.0, caso contrário, 0.0
    pct = step(0.45, pct);
    vec3 color = vec3(1.0-pct);
    gl_FragColor = vec4( color, 1.0 );
}