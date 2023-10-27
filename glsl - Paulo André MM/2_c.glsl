#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;

float plota(vec2 st, float pct, float qtd){
    float v1 = smoothstep( pct-qtd, pct, st.y);
    float v2 = smoothstep( pct, pct+qtd, st.y);
    return v1-v2;
}

void main() {
    vec2 st = gl_FragCoord.xy/u_resolution;
    st *= 4.0;//aumenta a área de visualização
    st -= 2.0;//desloca o gráfico da função

    float y = sin(3.0*st.x);
    // Desenha uma linha
    float valor = plota(st, y, 0.35);
    float valor2 = plota(st, y, 0.03);

    vec3 color = valor*vec3(1.0, 0.0, 0.0);
    color += valor2*vec3(1,1,1);
    

    gl_FragColor = vec4(color,1.0);
}