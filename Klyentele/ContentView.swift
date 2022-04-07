//
//  ContentView.swift
//  Klyentele
//
//  Created by Devin B on 4/6/22.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack () {
            VStack(alignment: .center)
            {
                //Logo
                Image("Logo")
                    .resizable(resizingMode: .stretch)
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 200, height: 200)
                //Text
                VStack(alignment: .leading) {
                    //Klyentele
                    Text("Klyentele").font(.custom("Montserrat", size: 48)).foregroundColor(.primary)
                    //by Azura4k
                    Text("by Azura4k").font(.custom("Montserrat", size: 14)).foregroundColor(.primary)
                }
                Spacer().frame(height: 30)
                
                Button("Next"){
                    
                }.buttonStyle(NormalButton())
                
                Button("About"){
                    
                }.buttonStyle(NormalButton())
                
                
                
            }
        }.frame(width:884,height: 647).background(.background)
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .preferredColorScheme(.light)
    }
}
