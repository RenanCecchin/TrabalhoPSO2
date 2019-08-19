#include<iostream>
#include<iomanip>
#include<fstream>
#include<vector> //vetores
#include<cmath>	//Importar cmath para usar sqrt e pow

struct Ponto
{
	float x;
	float y;

	float distancia(Ponto& p1) const{	//retorna a distancia de outro ponto a esse ponto
		return std::sqrt(std::pow((x-p1.x),2) + 
			std::pow((y-p1.y),2));
	}
};
int main(void) 
{
	Ponto p1, p2;
    std::string numero, aux;
    std::vector<float> pontos;
    std::ifstream entrada("pontos.txt");

    if(entrada.is_open() == false)
    	throw std::runtime_error{"Erro no arquivo"};

    while(entrada.eof() == false){
    	std::getline(entrada, numero);
    	for(auto i = 0; i < numero.length(); i++){
    		if(numero[i] == ' ' || i+1 == numero.length()){
    			float coordenada = std::stof(aux);
    			pontos.push_back(coordenada);
    			aux.clear();
    		}
    		else
    			aux += numero[i];
    	}
    }
    for(auto i = 0; i < pontos.size(); i++){
    	p1.x = pontos[i];
    	i++;
    	p1.y = pontos[i];
    	i++;
    	p2.x = pontos[i];
    	i++;
    	p2.y = pontos[i];
    	std::cout << std::fixed << std::setprecision(2) << "Distancia " << (i+1)/4 << " " << p1.distancia(p2) << std::endl;
    }
    std::cout << "Finished" << std::endl;
    return 0;
}