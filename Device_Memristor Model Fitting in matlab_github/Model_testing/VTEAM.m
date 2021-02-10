%%  VTEAM model 

%Model name: model of Memristor based on Theoretical formulas
%           this model was written by Dmitry Fliter and Keren Talisveyberg 
%           Technion Israel institute of technology EE faculty December 2011


model = 4;   % define the model 0 - Linear Ion Drift ; 1 - Simmons Tunnel Barrier; 2 - Team model ; 3 - Nonlinear Ion Drift model
win   = 0;   % define the window type :  0 - No window; 1 - Jogelkar window ; 2 - Biolek window ; 3 - Prodromakis window ; 4- Kvatinsky window (Team model only) 
iv    = 0;   % IV_relation=0 means linear V=IR. IV_relation=1 means nonlinear V=I*exp{..}  

%Genaral parameters
num_of_cycles = 20;
amp = 1;
freq = 2e6;
w_init = 0.5; % the initial state condition [0:1] 
D = 3e-09;
V_t = 0;
P_coeff = 2;
J = 1;
Roff = 2e3;
Ron = 100;


%Simmons Tunnel Bariier % Team parameters
a_on = 2e-09;
a_off = 5e-09;
c_on = 40e-03;
c_off = 3.5e-06;
alpha_on = 3;
alpha_off = 3;
k_on = -8e-5;
k_off = 8e-5;
i_on = 8.9e-06;
i_off = 115e-06;
v_on= 0.02;
v_off=-0.02;
x_on = 3e-09;
x_off = 0;
X_c = 107e-12;
b = 500e-06;



if (model==4)
points=2e5;
tspan=[0 num_of_cycles/freq];
t = linspace(tspan(1),tspan(2),points);
v = amp*sin(freq*2*pi*t);
X=zeros(1,points);
X_dot=zeros(1,points);
delta_t=t(2)-t(1);

X(1)=w_init*D;
     
for i=2:(length(t))
    % case this is an ideal window
    if (win == 0) 
          
          if (v(i) > 0) && (v(i) > v_off)
               X_dot(i)=k_off*(v(i)/v_off-1)^alpha_off;
               X(i)=X(i-1)+delta_t*X_dot(i);
          elseif (v(i) <= 0) && (v(i) < v_on)
               X_dot(i)=k_on*(v(i)/v_on-1)^alpha_on;
               X(i)=X(i-1)+delta_t*X_dot(i);
          else
               X(i)=X(i-1);
               X_dot(i)=0;
          end
    end
    
    % case this is Jogelkar window
    if (win == 1) 
          if (v(i) > 0) && (v(i) > v_off)
               X_dot(i)=k_off*(v(i)/v_off-1)^alpha_off;
               X(i)=X(i-1)+delta_t*X_dot(i).*(1-(2*X(i-1)/D-1)^(2*P_coeff));
          elseif (v(i) <= 0) && (v(i) < v_on)
               X_dot(i)=k_on*(v(i)/v_on-1)^alpha_on;
               X(i)=X(i-1)+delta_t*X_dot(i).*(1-(2*X(i-1)/D-1)^(2*P_coeff));
          else
               X(i)=X(i-1);
               X_dot(i)=0;
          end
    end
    
    % case this is Biolek window
    if (win == 2) 
          if (v(i) > 0) && (v(i) > v_off)
               X_dot(i)=k_off*(v(i)/v_off-1)^alpha_off;
               X(i)=X(i-1)+delta_t*X_dot(i).*(1-(1-X(i-1)/D-heaviside(v(i)))^(2*P_coeff));
          elseif (v(i) <= 0) && (v(i) < v_on)
               X_dot(i)=k_on*(v(i)/v_on-1)^alpha_on;
               X(i)=X(i-1)+delta_t*X_dot(i).*(1-(1-X(i-1)/D-heaviside(v(i)))^(2*P_coeff));
          else
               X(i)=X(i-1);
               X_dot(i)=0;
          end
    end
    
    % case this is Prodromakis window
    if (win == 3)
          if (v(i) > 0) && (v(i) > v_off)
               X_dot(i)=k_off*(v(i)/v_off-1)^alpha_off;
               X(i)=X(i-1)+delta_t*X_dot(i).*(J*(1-((X(i-1)/D-0.5)^2+0.75)^P_coeff));
          elseif (v(i) <= 0) && (v(i) < v_on)
               X_dot(i)=k_on*(v(i)/v_on-1)^alpha_on;
               X(i)=X(i-1)+delta_t*X_dot(i).*(J*(1-((X(i-1)/D-0.5)^2+0.75)^P_coeff));
          else
               X(i)=X(i-1);
               X_dot(i)=0;
          end
    end
    
    % case this is Kvatinsky window
    if (win == 4)
          if (v(i) > 0) && (v(i) > v_off)
               X_dot(i)=k_off*(v(i)/v_off-1)^alpha_off*exp(-exp((X(i-1)-a_off)/X_c));
               X(i)=X(i-1)+delta_t*X_dot(i);
          elseif (v(i) <= 0) && (v(i) < v_on)
               X_dot(i)=k_on*(v(i)/v_on-1)^alpha_on*exp(-exp(-(X(i-1)-a_on)/X_c));
               X(i)=X(i-1)+delta_t*X_dot(i);
          else
               X(i)=X(i-1);
               X_dot(i)=0;
          end
    end
     
    if (X(i) < 0)
        X(i) = 0;
        X_dot(i)=0;
    elseif (X(i) > D)
        X(i) = D;
        X_dot(i)=0;
    end


end

    if (iv == 0) %case I-V relation is linear
       R=Roff.*X./D+Ron.*(1-X./D);
       curr=v./R;
    else %case the I-V relation is nonlinear
       lambda = log(Roff/Ron);
       curr=v./(Ron.*exp(lambda*(X-x_on)/(x_off-x_on)));
    end
    
figure(1);    
plot(v(20e3:end),curr(20e3:end));
title('I-V curve');
xlabel('V[volt]');
ylabel('I[amp]');

figure(2);
plot(t,X/D);
title('X/D as func of time');
xlabel('time[sec]');
legend('X/D');

end